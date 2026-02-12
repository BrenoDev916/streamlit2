import streamlit as st

# Título da calculadora
st.title("Calculadora Simplest")

# Entrada de números
num1 = st.number_input("Digite o primeiro número", value=0.0)
operation = st.selectbox("Operação", ["+", "-", "*", "/"])
num2 = st.number_input("Digite o segundo número", value=0.0)

# Lógica da calculadora
result = 0
if st.button("Calcular"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Erro: Divisão por zero!")
            result = "Indefinido"
    
    # Exibe o resultado
    st.success(f"Resultado: {result}")

