import { readFileSync, writeFileSync } from "node:fs";

// ponytail: post-render hack because RenderCV can't scope a header link to HTML-only.
// Inserts one <li> PDF link into the connections list. Relative href → works locally and on gh-pages.
const targets = [
  { html: "build/index.html", pdf: "Fabrizio_Dante_Pauselli.pdf", label: "Download PDF" },
  { html: "build/es.html", pdf: "Fabrizio_Dante_Pauselli_ES.pdf", label: "Descargar PDF" },
];

for (const { html, pdf, label } of targets) {
  let src = readFileSync(html, "utf8");
  const li = `<li><a id="pdf-download" href="${pdf}">${label}</a></li>\n        `;
  // First </ul> closes the header connection list.
  src = src.replace("</ul>", li + "</ul>");
  // ponytail: RenderCV's markdown Header template strips ALL slashes from the
  // website display text (fpaus.github.iocv). href is fine; fix the visible text.
  src = src.replaceAll(">fpaus.github.iocv<", ">fpaus.github.io/cv<");
  writeFileSync(html, src);
}
