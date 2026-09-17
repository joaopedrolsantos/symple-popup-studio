import * as React from "react";

/**
 * Small uppercase meta chip — labels a swatch's role, a product trait ("auto", "fem", "macro"), a section.
 * Intentional addition — used throughout the guideline frames but not a Figma component.
 */
export interface TagProps extends React.HTMLAttributes<HTMLSpanElement> {
  children?: React.ReactNode;
  /** Fill/ink pairing. Default "on-dark". */
  tone?: "on-dark" | "on-light" | "accent" | "highlight";
}

export declare function Tag(props: TagProps): JSX.Element;
