export type CaptureInput = {
  text: string;
  source?: string;
  save?: boolean;
};

export async function captureToInbox(input: CaptureInput) {
  return {
    ok: true,
    stage: "capture",
    target: "inbox",
    input
  };
}

export async function normalizeNote(path: string) {
  return { ok: true, stage: "normalize", path };
}

export async function routeToMoc(path: string) {
  return { ok: true, stage: "route", path };
}

export async function runWeeklyAudit() {
  return { ok: true, stage: "weekly-audit" };
}
