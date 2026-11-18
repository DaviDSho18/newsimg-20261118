You are building a make.fun competition entry in this repository. Work in explicit narrated steps: before each step, write one short paragraph of plain text saying what you are about to do and why. Produce a separate text message for each step.

The competition: "Sum up 18 November's world news in one image". Your program writes ONE image to /output/entry.png that sums up the world's news of Wednesday 18 November 2026. The judge is an AI that can see images and has no news feed; it ranks by what the image itself shows. The image must name the day and show the day's real events, across regions, and stay legible at about 300 pixels across.

The image file `entry.png` already exists in this repository (1024x1024, a newspaper front page naming 18 November 2026 with the day's stories). Your job is to write the PROGRAM, `main.ts`, that the grader runs: it must copy `entry.png` to the output directory. The grader runs it in a fresh container with a read-only /bot (this repository at the submitted commit) and a writable /output, Node 22, standard library only, no network. Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output.

Step 1 — Plan: say what the program must do (copy entry.png to the output directory) and how you will make it robust (resolve the repo path from the module URL, fall back to /output, create the output directory if it is missing, verify the copy).

Step 2 — First draft: write main.ts in your own words. Use only node: standard library modules (node:fs, node:path, node:url). Read the source image from beside the module, write it to the output directory, and print a short confirmation line. Do not copy the kit's starter file verbatim.

Step 3 — Run and inspect: run it with `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts` and confirm out/entry.png was written with the same bytes as entry.png (compare sizes; use cmp or a checksum).

Step 4 — Revise: make one distinct improvement to main.ts (for example, create the output directory if absent with mkdirSync recursive, and fail loudly with a clear message if the source image is missing). This must be a real edit to main.ts.

Step 5 — Verify: run the program a second time and confirm both runs write identical bytes. Print the byte count.

Step 6 — Document: write README.md at the repository root explaining what the entry is (a one-image summary of 18 November 2026 world news), how the program works, and how to run it locally.

Keep every edit inside this repository. Do not touch .makefun/ or LICENSE. When done, print a one-line summary.
