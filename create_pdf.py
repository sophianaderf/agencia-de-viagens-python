from io import BytesIO

from fpdf import FPDF
from fpdf.fonts import FontFace


def criar_pdf(reservas):
    pdf = FPDF(
        orientation="L",
        unit="mm",
        format="A4",
    )
    pdf.add_page()
    pdf.set_margins(left=10, top=12, right=10)
    pdf.set_font("Helvetica", style="B", size=16)
    pdf.set_text_color(22, 50, 79)
    pdf.cell(
        w=0,
        h=10,
        text="Relatório de Reservas",
        align="C",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.set_font("Helvetica", size=9)
    pdf.set_text_color(70, 80, 90)
    pdf.ln(5)
    pdf.cell(
        w=0,
        h=6,
        text=f"Total de reservas: {len(reservas)}",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.ln(4)

    colunas = (
        ("ID", 0.06),
        ("Data", 0.10),
        ("Pessoas", 0.09),
        ("Cliente", 0.23),
        ("Pacote", 0.27),
        ("Agente responsável", 0.25),
    )
    with pdf.table(
        width=pdf.epw,
        col_widths=tuple(proporcao for _, proporcao in colunas),
        headings_style=FontFace(
            emphasis="BOLD",
            color=(22, 50, 79),
            fill_color=(232, 239, 244),
        ),
        line_height=7,
        text_align=("CENTER", "CENTER", "CENTER", "LEFT", "LEFT", "LEFT"),
    ) as tabela:
        tabela.row(tuple(titulo for titulo, _ in colunas))
        for reserva in reservas:
            data_reserva = reserva["data_reserva"]
            if hasattr(data_reserva, "strftime"):
                data_reserva = data_reserva.strftime("%d/%m/%Y")
            tabela.row(
                (
                    str(reserva["id"]),
                    str(data_reserva),
                    str(reserva["quantidade_pessoas"]),
                    str(reserva["cliente_nome"]),
                    str(reserva["nome_pacote"]),
                    str(reserva["func_nome"]),
                )
            )

    if not reservas:
        pdf.set_font("Helvetica", style="I", size=10)
        pdf.cell(
            w=0,
            h=8,
            text="Nenhuma reserva cadastrada.",
            new_x="LMARGIN",
            new_y="NEXT",
        )

    return BytesIO(pdf.output())

