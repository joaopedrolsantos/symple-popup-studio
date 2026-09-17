import * as React from 'react';
export interface TextFieldProps {
  className?: string;
  style?: React.CSSProperties;
  style2?: "filled" | "outlined";
  state?: "enabled" | "hovered" | "focused" | "error" | "disabled";
  textConfigurations?: "input-text" | "label-text" | "placeholder-text";
  leadingIcon?: boolean;
  trailingIcon?: boolean;
  showSupportingText?: boolean;
  supportingText?: string;
  labelText?: string;
  inputText?: string;
  placeholderText?: string;
  /** Swappable nested instance; defaults to the design's. */
  icon1?: React.ReactNode;
  /** Swappable nested instance; defaults to the design's. */
  icon2?: React.ReactNode;
}
export declare const TextField: React.FC<TextFieldProps>;
export default TextField;
