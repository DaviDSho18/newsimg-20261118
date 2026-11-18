import { copyFileSync, existsSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const currentDirectory = dirname(fileURLToPath(import.meta.url));
const sourceImage = join(currentDirectory, "entry.png");
const outputDirectory = process.env.MAKEFUN_OUTPUT_DIR || "/output";
const targetImage = join(outputDirectory, "entry.png");

// Ensure source image exists before attempting copy
if (!existsSync(sourceImage)) {
  console.error(`Error: Source news image not found at ${sourceImage}`);
  process.exit(1);
}

// Ensure output directory exists
mkdirSync(outputDirectory, { recursive: true });

// Copy image to destination
copyFileSync(sourceImage, targetImage);

// Validate copy and verify byte count matches
if (!existsSync(targetImage)) {
  console.error(`Error: Destination file ${targetImage} was not created`);
  process.exit(1);
}

const sourceStats = statSync(sourceImage);
const targetStats = statSync(targetImage);

if (sourceStats.size !== targetStats.size) {
  console.error(
    `Error: Size mismatch between source (${sourceStats.size}B) and target (${targetStats.size}B)`
  );
  process.exit(1);
}

console.log(
  `Successfully copied entry.png (${targetStats.size} bytes) to ${targetImage}`
);
