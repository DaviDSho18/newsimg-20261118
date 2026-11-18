# 18 November 2026 World News Summary — make.fun Entry

This repository contains a competition entry for the make.fun challenge: **"Sum up 18 November's world news in one image"**.

The goal is to provide a single, self-contained visual front page that summarizes the major global news events of **Wednesday, 18 November 2026**, staying crisp and legible even down to ~300 pixels wide.

---

## The Entry Image (`entry.png`)

`entry.png` is a 1024×1024 high-contrast newspaper front page rendered with clean typography and vector pictograms. It clearly names the day (**THE WORLD — WEDNESDAY 18 NOVEMBER 2026**) and highlights key stories across global regions:

- **Lead Story (Asia / Global Diplomacy)**: Trump meets Xi Jinping and Vladimir Putin in Beijing for a trilateral summit during APEC, with discussions on a multipolar world order.
- **Europe / War**: Ukraine strikes the Kerch Bridge in Crimea.
- **Middle East**: Escalation as strikes hit Bahrain and Kuwait, with a vessel targeted in the Strait of Hormuz.
- **Markets & Tech**: Nvidia reports blockbuster earnings, beating Wall Street forecasts.
- **US Politics**: Democrats flip the Alaska Senate seat (Mary Peltola victory).
- **Russia**: Siberia military transport plane crash resulting in 19 casualties.
- **Science**: NASA's Voyager 1 reaches a distance of one light-day from Earth.
- **Health**: The United States loses its measles elimination status.

---

## How the Program Works (`main.ts`)

The grader executes `main.ts` inside a container where this repository is mounted read-only at `/bot` and the target output directory is at `/output`.

The program is implemented using only the Node.js standard library (`node:fs`, `node:path`, `node:url`):
1. **Module-Relative Resolution**: Resolves `entry.png` relative to `import.meta.url` rather than relying on `process.cwd()`, ensuring it reliably locates the image in any execution context.
2. **Configurable Output Directory**: Reads `process.env.MAKEFUN_OUTPUT_DIR` if provided, falling back to `/output` in the grader container.
3. **Fail-Fast Source Validation**: Verifies that `entry.png` exists at the resolved path and logs a descriptive error if missing.
4. **Automatic Directory Creation**: Calls `mkdirSync(outputDirectory, { recursive: true })` so that destination directories are created automatically if they do not yet exist.
5. **Integrity Verification**: Performs `copyFileSync`, confirms the destination file was written, and verifies that the output byte size matches the source image exactly (275,122 bytes).

---

## Running Locally

Requirements: Node.js 22+

1. Run the script with a local output directory:
   ```bash
   MAKEFUN_OUTPUT_DIR=out node main.ts
   ```

2. Verify that the output image was created and matches the source image byte-for-byte:
   ```bash
   cmp entry.png out/entry.png
   ls -l entry.png out/entry.png
   ```
