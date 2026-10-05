#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
const strict = args.includes('--strict');
const fileArg = args.find((arg) => !arg.startsWith('--'));

if (!fileArg) {
  console.error('Usage: node validate_deck.js <deck.html> [--strict]');
  process.exit(2);
}

const deckPath = path.resolve(fileArg);
const deckDir = path.dirname(deckPath);
const html = fs.readFileSync(deckPath, 'utf8');
const errors = [];
const warnings = [];

const count = (regex) => (html.match(regex) || []).length;

// Inline JavaScript syntax.
for (const match of html.matchAll(/<script\b(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/gi)) {
  try {
    new Function(match[1]);
  } catch (error) {
    errors.push(`Inline JavaScript syntax error: ${error.message}`);
  }
}

// Duplicate IDs.
const ids = [...html.matchAll(/\bid=["']([^"']+)["']/gi)].map((match) => match[1]);
const duplicateIds = [...new Set(ids.filter((id, index) => ids.indexOf(id) !== index))];
if (duplicateIds.length) errors.push(`Duplicate IDs: ${duplicateIds.join(', ')}`);

// Coarse structural balance catches common editing mistakes.
const sectionOpen = count(/<section\b/gi);
const sectionClose = count(/<\/section>/gi);
if (sectionOpen !== sectionClose) errors.push(`Unbalanced <section> tags: ${sectionOpen} open, ${sectionClose} close`);

const slides = [...html.matchAll(/<section\b([^>]*\bclass=["'][^"']*\bslide\b[^"']*["'][^>]*)>/gi)];
if (!slides.length) warnings.push('No <section class="slide"> elements found');
for (const [index, slide] of slides.entries()) {
  if (!/\bid=["'][^"']+["']/i.test(slide[1])) errors.push(`Static slide ${index + 1} has no unique id`);
}

// Local asset references in HTML and CSS url(...).
const refs = new Set();
for (const match of html.matchAll(/\b(?:src|poster|href)=["']([^"']+)["']/gi)) refs.add(match[1]);
for (const match of html.matchAll(/url\(\s*["']?([^"')]+)["']?\s*\)/gi)) refs.add(match[1]);

const isRemoteOrVirtual = (ref) =>
  /^(?:https?:|data:|blob:|mailto:|tel:|javascript:|#|\/\/)/i.test(ref) ||
  ref.startsWith('var(');

for (const rawRef of refs) {
  const cleanRef = decodeURIComponent(rawRef.split('#')[0].split('?')[0]);
  if (!cleanRef || isRemoteOrVirtual(cleanRef)) continue;
  const assetPath = path.resolve(deckDir, cleanRef);
  if (!fs.existsSync(assetPath)) errors.push(`Missing local asset: ${rawRef}`);
}

// Heuristics: warnings require visual judgment, not blind replacement.
const tinyFonts = [...html.matchAll(/font-size\s*:\s*([0-9.]+)px/gi)]
  .map((match) => Number(match[1]))
  .filter((size) => size > 0 && size < 10);
if (tinyFonts.length) {
  warnings.push(`${tinyFonts.length} CSS font-size declaration(s) are below 10px; verify they are nonessential labels`);
}

const coverCount = count(/object-fit\s*:\s*cover/gi);
if (coverCount) {
  warnings.push(`${coverCount} object-fit: cover declaration(s) found; verify each is decorative or explicitly approved`);
}

const slideNumbers = count(/class=["'][^"']*\bslide-no\b/gi);
if (slides.length && slideNumbers !== slides.length) {
  warnings.push(`Static slide/page-number count differs: ${slides.length} slides, ${slideNumbers} slide-number elements`);
}

console.log(`Deck: ${deckPath}`);
console.log(`Static slides: ${slides.length}`);
console.log(`IDs: ${ids.length} (${duplicateIds.length ? 'duplicates found' : 'unique'})`);
console.log(`Local/remote references scanned: ${refs.size}`);

if (warnings.length) {
  console.log('\nWarnings:');
  for (const warning of warnings) console.log(`- ${warning}`);
}

if (errors.length) {
  console.error('\nErrors:');
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log('\nStatic validation passed. Visual 16:9 review is still required.');
if (strict && warnings.length) process.exit(3);
