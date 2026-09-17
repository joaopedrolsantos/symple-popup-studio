import * as React from "react";

/**
 * The Seed Supreme wordmark / isologo, in the four lockups supplied with the brand.
 * Kit families: `LOGO BLACK` + `isologo`.
 */
export interface LogoProps extends React.ImgHTMLAttributes<HTMLImageElement> {
  /** Which lockup to render. Default "horizontal". */
  variant?: "horizontal" | "horizontal-reduced" | "vertical" | "symbol";
  /** "dark" = Brown/black ink for light surfaces; "white" = knockout for dark surfaces. Default "dark". */
  tone?: "dark" | "white";
  /** Rendered height in px; width follows the lockup's native ratio. Default 148. */
  height?: number;
  /** Path prefix for the logo SVGs. Default "/assets/logo". */
  assetBase?: string;
  /** Alt text. Default "Seed Supreme". */
  title?: string;
}

export declare function Logo(props: LogoProps): JSX.Element;
