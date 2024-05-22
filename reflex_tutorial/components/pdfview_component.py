import reflex as rx


class PdfView(rx.Component):
    library = "react-pdf"
    # workerUrl = "https://unpkg.com/pdfjs-dist@3.4.120/build/pdf.worker.min.js"
    tag = "Document"
    file = "./prueba.pdf"
    options = {
        "height": "800px",
        "width": "800px"
    }


pdfview = PdfView.create