import pandas as pd
import streamlit as st

# Carregar os dados da planilha
#tabela = pd.read_excel(r"B:\24 - Inteligencia\planilha meta king 50 anos.xlsx")
tabela = pd.read_csv(f"https://docs.google.com/spreadsheets/d/1EfLHMs8AQ9NFflQpQd8qZer6yHVo0gQTUKxGGisy6Co/export?format=csv", decimal=",")
tabela["Faturamento Total"] = tabela["Faturamento Total"].fillna("R$ 0,00")

# Configuração inicial do Streamlit
st.set_page_config(
    page_title="Clientes VIP LLE",
    page_icon="💎",
    layout="wide",
)

# 🔹 **Manter o layout original da primeira página**
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

# 🔹 Função para verificar cliente
def verificar_cliente(cod_matriz):
    try:
        nome = tabela.loc[tabela["Cod_Matriz"] == cod_matriz, "Nome Matriz"].values[0]
        return f"**Grupo econômico encontrado:** {cod_matriz} - {nome}"
    except:
        return "🚨 Cliente não encontrado! Verifique o código da matriz."

# 🔹 **Primeira página (Corrigindo alinhamento)**
if st.session_state.pagina == "inicio":
    st.markdown(
        """
        <style>

    /* Botão st.button */
    div.stButton > button {
        height: 38px !important;
        line-height: 38px !important;
        padding: 0 20px !important;
        font-size: 16px !important;
        color: #fff !important;
        background-color: #262626 !important;
        border: none !important;
        border-radius: 5px !important;
        cursor: pointer !important;
        width: 100% !important; /* se quiser ocupar o espaço da coluna */
        margin: 0 !important;  /* retira margens extras */
        transition: background-color 0.3s ease !important;
    }
    div.stButton > button:hover {
        background-color: #0a0a0a !important;
        border: none !important;
        box-shadow: none !important;
        color: white !important; /* Mantém a cor do texto branca */
    }

    /* Para st.link_button (caso gere <a> em vez de <button>) */
    div.stLinkButton {
        display: flex !important; /* Torna o container flexível */
        justify-content: center !important; /* Centraliza horizontalmente o botão */
        align-items: center !important; /* Centraliza verticalmente o botão */
    }

    div.stLinkButton > a {
        height: auto !important; /* Adapta a altura ao conteúdo */
        line-height: normal !important; /* Ajusta para centralizar o texto corretamente */
        font-size: 34px !important; /* Aumentado em 4px */
        font-weight: bold !important; /* Texto em negrito */
        color: #fff !important;
        background-color: #262626 !important;
        border: none !important;
        padding: 10px 20px !important; /* Espaçamento interno */
        cursor: pointer !important;
        border-radius: 5px !important;
        transition: background-color 0.3s ease !important;
        text-align: center !important; /* Centraliza o texto */
        text-decoration: none !important; /* Remove sublinhado */
        margin: 0 auto !important; /* Centraliza o botão na página */
        width: auto !important; /* Adapta a largura ao texto */
        max-width: 100% !important; /* Evita ultrapassar a largura da tela */
    }

    /* Efeito hover */
    div.stLinkButton > a:hover {
        background-color: #0a0a0a !important;
    }

    /* Estilo responsivo para telas menores */
    @media (max-width: 768px) {
        div.stLinkButton > a {
            font-size: 30px !important; /* Ajusta o tamanho da fonte no mobile */
            width: 100% !important; /* Largura 100% no mobile */
            margin: 10px 0 !important; /* Margem vertical no mobile */
            word-wrap: break-word !important; /* Permite quebra de texto */
            white-space: normal !important; /* Permite múltiplas linhas */
        }
    }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([0.5,2,0.5])


    with col2:
        #st.image("https://iili.io/3CuR93B.jpg")
        st.subheader("Bem-vindo (a) ao portal de consulta.", "center")
        st.write("Digite o código da matriz do seu grupo econômico:")
        col11, col22 = st.columns([2,1.3])
        with col11:
            codigo = (st.number_input(label = "",label_visibility="collapsed", value = None,format="%0.0f", placeholder="Digite o código de matriz do seu grupo econômico"))

        if codigo == None:
            pass
        else:
            codigo = int(codigo)

        with col22:
            confirmacao = st.button("Confirmar código")

        if confirmacao and codigo:
            nome_cliente = verificar_cliente(codigo)
            if nome_cliente:
                st.session_state.codigo_cliente = codigo
                st.session_state.pagina = "detalhes"
                st.rerun()

# 🔹 **Segunda página (Mantendo layout estilizado)**
elif st.session_state.pagina == "detalhes":
    # Injetar estilos apenas na segunda página para manter o layout da primeira inalterado
    st.markdown("""
        <style>
                
            .styled-table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-size: 16px;
                text-align: left;
                border-radius: 10px;
                overflow: hidden;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }

            .styled-table thead tr {
                background-color: #262626;
                color: white;
                text-align: left;
            }

            .styled-table th, .styled-table td {
                padding: 12px 15px;
                border: 1px solid #ddd;
            }

            .highlight {
                background-color: #DFF0D8;
                font-weight: bold;
            }

            .black-background {
                background-color: #262626;
                color: white;
                font-weight: bold;
            }

            .bold-text {
                font-weight: bold;
            }

            .stButton > button {
                width: 100%;
                padding: 12px;
                font-size: 18px;
                font-weight: bold;
                background-color: #262626;
                color: white;
                border-radius: 8px;
            }

            .stButton > button:hover {
                background-color: #0a0a0a;
                border: none !important;
                box-shadow: none !important;
                color: white !important; /* Mantém a cor do texto branca */
            }
        </style>
    """, unsafe_allow_html=True)

    #st.image("https://iili.io/3CuR93B.jpg", width = 1760)

    # Pega os dados do cliente
    codigo_cliente = st.session_state.codigo_cliente
    dados_cliente = tabela[tabela["Cod_Matriz"] == codigo_cliente]

    if not dados_cliente.empty:
        nome_matriz = dados_cliente["Nome_Matriz"].values[0]
        meta = dados_cliente["Meta"].values[0]
        faturado = dados_cliente["Faturamento Total"].values[0]
        percentual = dados_cliente["% Alcançado"].values[0]
        valor_falta = dados_cliente["Valor que falta"].values[0]
        situacao = dados_cliente["Situação"].values[0]
        cashback = dados_cliente["Cashback"].values[0]
        ultima_atualizacao = dados_cliente["Última Atualização"].values[0]

        # 🔹 **Seção de Identificação do Cliente**
        st.markdown("### 🏷️ Identificação do Cliente")
        st.markdown(f"""
            <table class="styled-table">
                <tr class="black-background">
                    <th>Código Cliente</th>
                    <th>Nome Matriz</th>
                </tr>
                <tr>
                    <td class="bold-text">{codigo_cliente}</td>
                    <td class="bold-text">{nome_matriz}</td>
                </tr>
            </table>
        """, unsafe_allow_html=True)

        # 🔹 **Seção de Meta**
        # Definir a cor do fundo com base na situação
        # 🔹 **Definir a cor do fundo com base na situação**
        cor_situacao = "#b5f09c" if situacao == "Dentro da meta" else "#FFCCCC"  # Verde para "Dentro da meta", Vermelho para outros

# 🔹 **Seção de Meta com fonte maior**
        st.markdown("### 🎯 Meta")
        st.markdown(f"""
    <style>
        .styled-table td, .styled-table th {{
            font-size: 18px;  /* Aumenta a fonte dos dados */
            padding: 14px;  /* Melhora o espaçamento */
        }}
    </style>
    <table class="styled-table">
        <tr class="black-background">
            <th>Meta Cliente VIP</th>
            <th>Faturado</th>
            <th>%</th>
            <th>Valor que falta</th>
            <th>Situação Atual</th>
        </tr>
        <tr>
            <td>{meta}</td>
            <td>{faturado}</td>
            <td>{str(f"{percentual}").replace(".", ",")}</td>
            <td>{valor_falta}</td>
            <td style="background-color: {cor_situacao}; font-weight: bold; text-align: center;">{situacao}</td>
        </tr>
    </table>
""", unsafe_allow_html=True)

        # 🔹 **Seção de Prêmio e Última Atualização**
        st.markdown("### 💵 Cashback e Última Atualização")
        st.markdown(f"""
            <table class="styled-table">
                <tr class="black-background">
                    <th>Prêmio (Cashback) - em caso de atingimento de meta</th>
                    <th>Última Atualização</th>
                </tr>
                <tr>
                    <td>{cashback}</td>
                    <td>{ultima_atualizacao}</td>
                </tr>
            </table>
        """, unsafe_allow_html=True)

        # 🔹 **Botão de Voltar**
        if st.button("🔙 Voltar"):
            st.session_state.pagina = "inicio"
            st.rerun()
    else:
        st.error("🚨 Nenhuma informação encontrada para este cliente.")
        if st.button("🔙 Voltar"):
            st.session_state.pagina = "inicio"
            st.rerun()
