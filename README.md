Monitor de Vazamento de Dados
Ferramenta de linha de comando em Python para verificar se e-mails aparecem em bases de dados vazadas, utilizando a API do HaveIBeenPwned. Gera relatórios em .csv para fins de auditoria e conformidade com a LGPD.

Funcionalidades

Consulta um ou múltiplos e-mails de uma vez
Exibe os vazamentos encontrados direto no terminal
Gera relatório .csv com timestamp único por execução
Tratamento de erros de conexão e autenticação
API Key protegida via variável de ambiente (.env)


Como usar
Pré-requisitos

Python 3.10+
Conta e API Key no HaveIBeenPwned

Instalação
1. Clone o repositório:
bashgit clone https://github.com/seu-usuario/monitor-vazamento.git
cd monitor-vazamento
2. Crie e ative o ambiente virtual:
bashpython -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
3. Instale as dependências:
bashpip install requests python-dotenv
4. Configure a API Key:
Crie um arquivo .env na raiz do projeto:
HIBP_API_KEY=sua_chave_aqui

Execução
Consultar um e-mail:
bashpython monitor.py usuario@exemplo.com
Consultar múltiplos e-mails:
bashpython monitor.py usuario@exemplo.com outro@exemplo.com
Ver ajuda:
bashpython monitor.py --help

Exemplo de saída
Configuração validada.

Consultando: test@example.com
----------------------------------------
3 vazamento(s) encontrado(s):
Adobe (2013-10-04)
LinkedIn (2016-05-05)
Canva (2019-05-24)

Relatório salvo: relatorio_20250429_143022.csv
Exemplo de relatório .csv gerado:
EmailServiçoData do VazamentoTotal AfetadosDescriçãotest@example.comAdobe2013-10-04152445165Dados de clientes Adobe expostos...test@example.comLinkedIn2016-05-05164611595Emails e senhas hash expostos...

Estrutura do projeto
monitor-vazamento/
├── monitor.py       # Script principal
├── .env             # API Key (não versionado)
├── .gitignore       # Arquivos ignorados pelo Git
└── README.md        # Este arquivo

Segurança

A API Key nunca é exposta no código-fonte
O arquivo .env está listado no .gitignore
Nenhum dado consultado é armazenado além do relatório local


Bibliotecas utilizadas
BibliotecaUsorequestsRequisições HTTP para a APIcsvGeração do relatóriojsonProcessamento da resposta da APIargparseArgumentos via terminalpython-dotenvLeitura segura da API KeydatetimeTimestamp nos relatórios

Conformidade LGPD
Este projeto foi desenvolvido com foco em conformidade com a Lei Geral de Proteção de Dados (LGPD — Lei nº 13.709/2018). A ferramenta permite que empresas e profissionais identifiquem proativamente e-mails corporativos expostos em vazamentos, apoiando processos de gestão de risco e resposta a incidentes.

Autor
Desenvolvido como projeto de estudo com foco em segurança da informação e boas práticas de desenvolvimento Python.
