import * as React from "react";

/**
 * The brand's primary action: Cinnamon→Bronze gradient, 16px radius, underlined Work Sans Bold label.
 * Intentional addition — the treatment appears on nine guideline frames but is not a Figma component.
 */
export interface GradientButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  /** Label text. */
  children?: React.ReactNode;
  /** Font Awesome glyph name for the accompanying icon, e.g. "download". */
  icon?: string;
  /** Which side the icon sits on. Default "end". */
  iconPosition?: "start" | "end";
  /** "lg" is the source size (32px label, 76px tall); "md"/"sm" scale it down proportionally. Default "lg". */
  size?: "lg" | "md" | "sm";
  /** "gradient" (default), flat "solid" Cinnamon, or "dark" Eerie Black. */
  tone?: "gradient" | "solid" | "dark";
  /** Underline the label, as the source does. Default true. */
  underline?: boolean;
  /** Render as an anchor instead of a button. */
  href?: string;
}

export declare function GradientButton(props: GradientButtonProps): JSX.Element;
