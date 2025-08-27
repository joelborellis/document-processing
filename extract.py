import pymupdf4llm

md_text = pymupdf4llm.to_markdown(
    doc="GO_PAAS_Matrix.pdf",
    page_chunks=False,
    write_images=True,
    image_path="images",
    image_format="png",
    dpi=300,
)

# Write markdown to file
with open("GO_PAAS_Matrix.md", "w", encoding="utf-8") as f:
    f.write("\n\n".join(md_text))
