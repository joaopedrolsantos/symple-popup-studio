import React from "react";
import { Icon } from "../icons/Icon.jsx";

/* The brand's action treatment, transcribed from the guideline frames: 16px radius,
   Cinnamon→Bronze gradient at 110.521deg, warm drop shadow + orange glow,
   Work Sans Bold label at -4% tracking, optional trailing icon. */
export function GradientButton({ children, icon, iconPosition = "end", size = "lg", tone = "gradient", underline = true, href, style, ...rest }) {
  const scale = size === "sm" ? 0.5 : size === "md" ? 0.72 : 1;
  const fill =
    tone === "solid" ? "var(--ss-cinnamon,#D1671B)" :
    tone === "dark" ? "var(--ss-eerie-black,#1A1A1A)" :
    "var(--gradient-button,linear-gradient(110.521deg,#D1671B 14.07%,#422109 89.20%))";
  const base = {
    display: "inline-flex", alignItems: "center", justifyContent: "center",
    gap: Math.round(16 * scale),
    padding: `${Math.round(20 * scale)}px ${Math.round(26 * scale)}px ${Math.round(20 * scale)}px ${Math.round(32 * scale)}px`,
    borderRadius: Math.max(8, Math.round(16 * scale)),
    border: "none", background: fill, cursor: "pointer",
    boxShadow: "var(--shadow-button,0px 24px 32px -24px rgba(8,23,14,0.88),0px 0px 32px 0px rgba(244,121,32,0.16))",
    fontFamily: "var(--font-body,'Work Sans',sans-serif)",
    fontWeight: 700, fontSize: Math.round(32 * scale), letterSpacing: "-0.04em", lineHeight: 1.2,
    color: "var(--ss-white,#fff)", textDecoration: "none",
    transition: "filter var(--motion-fast,160ms) var(--motion-ease,ease), transform var(--motion-fast,160ms) var(--motion-ease,ease)",
    ...style
  };
  const label = (
    <span style={{ textDecoration: underline ? "underline" : "none", textShadow: "var(--shadow-text-glow,0px 0px 8px rgba(255,255,255,0.24))" }}>{children}</span>
  );
  const glyph = icon ? <Icon name={icon} size={Math.round(32 * scale)} color="var(--ss-white,#fff)" padding="none" glow /> : null;
  const content = iconPosition === "start" ? [glyph, label] : [label, glyph];
  const Tag = href ? "a" : "button";
  return (
    <Tag href={href} style={base} {...rest}>
      {content.map((c, i) => (c ? <React.Fragment key={i}>{c}</React.Fragment> : null))}
    </Tag>
  );
}
