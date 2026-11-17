from io import BytesIO

from fpdf import FPDF
from fpdf.fonts import FontFace


def criar_pdf(reservas):
    colunas = (
        ("ID", 0.06),
        ("Data", 0.10),
        ("Pessoas", 0.09),
        ("Cliente", 0.23),
        ("Pacote", 0.27),
        ("Agente responsável", 0.25),
    )
    linhas = (
        (
            str(reserva["id"]),
            _formatar_data(reserva["data_reserva"]),
            str(reserva["quantidade_pessoas"]),
            str(reserva["cliente_nome"]),
            str(reserva["nome_pacote"]),
            str(reserva["func_nome"]),
        )
        for reserva in reservas
    )
    return _criar_pdf_relatorio(
        "Relatório de Reservas",
        "reservas",
        reservas,
        colunas,
        linhas,
        "Nenhuma reserva cadastrada.",
        ("CENTER", "CENTER", "CENTER", "LEFT", "LEFT", "LEFT"),
    )


def criar_pdf_pagamentos(pagamentos):
    colunas = (
        ("ID", 0.05),
        ("ID Reserva", 0.08),
        ("Valor total", 0.14),
        ("Forma", 0.17),
        ("Parcelas", 0.10),
        ("Valor parcela", 0.14),
        ("Data", 0.13),
        ("Status", 0.19),
    )
    linhas = (
        (
            str(pagamento["id"]),
            f"#{pagamento['id_reserva']}",
            f"R$ {pagamento['valor_total']:.2f}",
            str(pagamento["forma_pagamento"]),
            f"{pagamento['quantidade_parcelas']}x",
            f"R$ {pagamento['valor_parcela']:.2f}",
            _formatar_data(pagamento["data_pagamento"]),
            str(pagamento["status"]),
        )
        for pagamento in pagamentos
    )
    return _criar_pdf_relatorio(
        "Relatório de Pagamentos",
        "pagamentos",
        pagamentos,
        colunas,
        linhas,
        "Nenhum pagamento cadastrado.",
        (
            "CENTER",
            "CENTER",
            "RIGHT",
            "LEFT",
            "CENTER",
            "RIGHT",
            "CENTER",
            "LEFT",
        ),
    )


def _formatar_data(valor):
    if hasattr(valor, "strftime"):
        return valor.strftime("%d/%m/%Y")
    return str(valor)


def _criar_pdf_relatorio(
    titulo,
    nome_registros,
    registros,
    colunas,
    linhas,
    mensagem_vazia,
    alinhamentos,
):
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.set_margins(left=10, top=12, right=10)
    pdf.add_page()
    pdf.set_font("Helvetica", style="B", size=16)
    pdf.set_text_color(22, 50, 79)
    pdf.cell(
        w=0,
        h=10,
        text=titulo,
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
        text=f"Total de {nome_registros}: {len(registros)}",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.ln(4)
    with pdf.table(
        width=pdf.epw,
        col_widths=tuple(proporcao for _, proporcao in colunas),
        headings_style=FontFace(
            emphasis="BOLD",
            color=(22, 50, 79),
            fill_color=(232, 239, 244),
        ),
        line_height=7,
        text_align=alinhamentos,
    ) as tabela:
        tabela.row(tuple(titulo for titulo, _ in colunas))
        for linha in linhas:
            tabela.row(linha)

    if not registros:
        pdf.set_font("Helvetica", style="I", size=10)
        pdf.cell(
            w=0,
            h=8,
            text=mensagem_vazia,
            new_x="LMARGIN",
            new_y="NEXT",
        )

    return BytesIO(pdf.output())

