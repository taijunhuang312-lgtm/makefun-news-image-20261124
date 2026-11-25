import { copyFile, mkdir, open, stat } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir = dirname(fileURLToPath(import.meta.url));
const entryName = "entry.png";

// First eight bytes of every PNG file: 89 50 4E 47 0D 0A 1A 0A.
const PNG_SIGNATURE = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

async function checkPngHeader(path: string): Promise<void> {
  const handle = await open(path, "r");
  try {
    const header = Buffer.alloc(PNG_SIGNATURE.length);
    const { bytesRead } = await handle.read(header, 0, header.length, 0);
    if (bytesRead !== PNG_SIGNATURE.length || !header.equals(PNG_SIGNATURE)) {
      throw new Error(`source file is not a PNG image: ${path}`);
    }
  } finally {
    await handle.close();
  }
}

async function main(): Promise<void> {
  const source = join(scriptDir, entryName);
  const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
  const target = join(outputDir, entryName);

  await checkPngHeader(source);

  await mkdir(outputDir, { recursive: true });
  await copyFile(source, target);

  const sourceSize = (await stat(source)).size;
  let targetSize: number;
  try {
    targetSize = (await stat(target)).size;
  } catch {
    throw new Error(`output file missing after copy: ${target}`);
  }
  if (targetSize === 0 || targetSize !== sourceSize) {
    throw new Error(
      `output file failed verification: ${target} is ${targetSize} bytes, expected ${sourceSize}`,
    );
  }

  console.log(`wrote ${targetSize} bytes to ${target}`);
}

main().catch((error: unknown) => {
  console.error(error instanceof Error ? error.message : error);
  process.exit(1);
});
