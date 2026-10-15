import { createHash } from "node:crypto";
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const scriptsDirectory = import.meta.dir;
const nodeModulesDirectory = join(scriptsDirectory, "node_modules");
const commanderPackagePath = join(
  nodeModulesDirectory,
  "commander",
  "package.json"
);
const installKeyPath = join(
  nodeModulesDirectory,
  ".poteto-mode-tools-install-key"
);

function currentInstallKey(): string {
  return createHash("sha256")
    .update(readFileSync(join(scriptsDirectory, "package.json")))
    .update("\0")
    .update(readFileSync(join(scriptsDirectory, "bun.lock")))
    .digest("hex");
}

export function ensureDependenciesInstalled(): void {
  const installKey = currentInstallKey();
  if (
    existsSync(commanderPackagePath) &&
    JSON.parse(readFileSync(commanderPackagePath, "utf8")).version === "14.0.0" &&
    existsSync(installKeyPath) &&
    readFileSync(installKeyPath, "utf8").trim() === installKey
  ) {
    return;
  }

  if (!existsSync(commanderPackagePath)) {
    throw new Error(
      "Missing commander. Review package.json and bun.lock, check dependency advisories, then explicitly run bun install --frozen-lockfile in the scripts directory. Automatic installation is disabled."
    );
  }
  if (
    JSON.parse(readFileSync(commanderPackagePath, "utf8")).version !== "14.0.0"
  ) {
    throw new Error(
      "Installed commander does not match the locked version 14.0.0. Explicitly restore the reviewed frozen lockfile before running this tool."
    );
  }

  // Dependencies must be restored explicitly; the key never authorizes an install.
  writeFileSync(installKeyPath, `${installKey}\n`);
}
