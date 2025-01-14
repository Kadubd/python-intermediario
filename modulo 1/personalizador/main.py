import argparse
from personalizador import layout, painel, progresso, estilo

def main():
    parser = argparse.ArgumentParser(description="Interface para personalização com Rich")
    parser.add_argument("texto", help="Texto ou arquivo a ser exibido")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o texto é um arquivo")
    parser.add_argument("-m", "--modulo", choices=["layout", "painel", "progresso", "estilo"], required=True, help="Escolha o módulo")
    parser.add_argument("-f", "--funcao", choices=["exibir_layout", "exibir_titulo", "exibir_painel_simples", 
                                                    "exibir_painel_colorido", "barra_progresso_simples", 
                                                    "barra_progresso_personalizada", "exibir_texto_estilizado", 
                                                    "exibir_texto_destacado"], required=True, help="Escolha a função")

    args = parser.parse_args()
    modulo = {
        "layout": layout,
        "painel": painel,
        "progresso": progresso,
        "estilo": estilo
    }[args.modulo]

    funcao = getattr(modulo, args.funcao)
    funcao(args.texto, args.arquivo)

if __name__ == "__main__":
    main()
