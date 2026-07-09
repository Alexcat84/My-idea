"use client";

/**
 * Markdown — render de los documentos del motor (planes, reportes) con
 * la tipografía del sistema: jerarquía por tamaño y peso, interlineado
 * generoso, el acento solo donde el contenido lo pide.
 */
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

export function Markdown({ children }: { children: string }) {
  return (
    <div
      className={
        "text-[15px] leading-relaxed " +
        "[&_h1]:text-xl [&_h1]:font-semibold [&_h1]:leading-snug [&_h1]:mt-1 [&_h1]:mb-3 " +
        "[&_h2]:text-lg [&_h2]:font-semibold [&_h2]:mt-6 [&_h2]:mb-2 " +
        "[&_h3]:text-base [&_h3]:font-semibold [&_h3]:mt-4 [&_h3]:mb-1.5 " +
        "[&_p]:my-2.5 [&_ul]:my-2.5 [&_ul]:list-disc [&_ul]:pl-5 [&_ol]:my-2.5 [&_ol]:list-decimal [&_ol]:pl-5 " +
        "[&_li]:my-1 [&_strong]:font-semibold [&_em]:text-dim [&_hr]:my-5 [&_hr]:border-hairline " +
        "[&_blockquote]:border-l-2 [&_blockquote]:border-hairline [&_blockquote]:pl-4 [&_blockquote]:text-dim"
      }
    >
      <ReactMarkdown remarkPlugins={[remarkGfm]}>{children}</ReactMarkdown>
    </div>
  );
}
