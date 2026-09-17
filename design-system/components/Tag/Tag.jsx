import React from "react";

/* The role/meta chip used throughout the guidelines: 8px radius, translucent black or
   white fill, uppercase Work Sans SemiBold 18px at -4% tracking. */
export function Tag({ children, tone = "on-dark", style, ...rest }) {
  const map = {
    "on-dark": { background: "var(--ss-black-24,rgba(0,0,0,0.24))", color: "var(--ss-white-64,rgba(255,255,255,0.64))" },
    "on-light": { background: "var(--ss-black-12,rgba(0,0,0,0.12))", color: "var(--ss-ink-64,rgba(26,26,26,0.64))" },
    accent: { background: "var(--ss-orange-16,rgba(244,121,32,0.16))", color: "var(--ss-tango-orange,#F47920)" },
    highlight: { background: "var(--ss-canary-yellow,#D4FF5C)", color: "var(--ss-eerie-black,#1A1A1A)" }
  };
  return (
    <span
      style={{
        display: "inline-flex", alignItems: "center", justifyContent: "center", gap: 8,
        padding: "10px 12px", borderRadius: 8,
        fontFamily: "var(--font-body,'Work Sans',sans-serif)", fontWeight: 600, fontSize: 18,
        letterSpacing: "-0.04em", lineHeight: 1.2, textTransform: "uppercase",
        ...(map[tone] || map["on-dark"]), ...style
      }}
      {...rest}
    >{children}</span>
  );
}
