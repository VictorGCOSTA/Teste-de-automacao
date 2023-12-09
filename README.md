
# Automatização de Compras com Selenium

Este guia fornecerá instruções passo a passo para executar o código Python fornecido, que automatiza o processo de compra em um site utilizando a biblioteca Selenium.

### Pré-requisitos:

1. **Python:** Verifique se o Python está instalado no seu sistema. Você pode baixá-lo em [Python.org](https://www.python.org/downloads/).
   
2. **Bibliotecas Python:** Instale as bibliotecas necessárias. Abra o terminal ou prompt de comando e execute o seguinte comando:

    ```bash
    pip install selenium xmltodict
    ```

3. **Driver do navegador:** Baixe o driver do Chrome e certifique-se de ter o executável na sua variável de ambiente PATH ou no mesmo diretório do script Python.

### Executando o Código:

1. **Clone ou Baixe o Código:**

   - Clone o repositório usando Git:

    ```bash
    git clone https://github.com/VictorGCOSTA/Teste-de-automacao.git
    ```
   
   - Ou baixe o arquivo ZIP e extraia-o.

2. **Configure o Arquivo XML:**

   - Configure o arquivo `user.xml` no mesmo diretório do script Python com as informações necessárias: `username`, `password`, `firstname`, `lastname` e `postalcode`.

3. **Execute o Script:**

   - Abra o terminal ou prompt de comando e navegue até o diretório onde o código está localizado:
    ```bash
    cd .\Teste-de-automacao\
   ```
   - Execute o script Python:
    ```bash
    python teste_automacao.py
    ```

4. **Observações:**

   - Certifique-se de ter uma conexão estável com a internet durante a execução do script.
   - O script automatizará o login, seleção de produtos, adição ao carrinho, preenchimento de informações de compra e finalização do processo.

