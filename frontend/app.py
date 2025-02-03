import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide")

st.image("logo.png", width=200)

st.title("Controle de Veículos")

def show_response_message(response):
    if response.status_code == 200:
        st.success("Operação realizada com sucesso!")
    else:
        try:
            data = response.json()
            if "detail" in data:
                if isinstance(data["detail"], list):
                    errors = "\n".join([error["msg"] for error in data["detail"]])
                    st.error(f"Erro: {errors}")
                else:
                    st.error(f"Erro: {data['detail']}")
        except ValueError:
            st.error("Erro desconhecido. Não foi possível decodificar a resposta.")


with st.expander("Adicionar um Novo Veículo"):
    with st.form("new_car"):
        model = st.text_input("Modelo do Veículo")
        brand = st.text_input("Marca do Veículo")
        model_year = st.number_input("Ano do Veículo",step=1)
        plate = st.text_input("Placa do Veículo")
        kilometers = st.number_input("Kilometragem do Veículo")
        status = st.selectbox(
            "Status",
            ["Novo", "Revisão necessária", "Em uso", "Manutenção necessária", "Parado"],
        )
        submit_button = st.form_submit_button("Adicionar Produto")

        if submit_button:
            response = requests.post(
                "http://backend:8000/cars/",
                json={
                    "model": model,
                    "brand": brand,
                    "model_year": model_year,
                    "plate": plate,
                    "kilometers": kilometers,
                    "status": status,
                },
            )
            show_response_message(response)


with st.expander("Visualizar Veículos"):
    if st.button("Exibir Todos os Veículos"):
        response = requests.get("http://backend:8000/cars/")
        if response.status_code == 200:
            product = response.json()
            df = pd.DataFrame(product)

            df = df[
                [
                    "car_id",
                    "model",
                    "brand",
                    "model_year",
                    "plate",
                    "kilometers",
                    "status",
                    "created_at",
                ]
            ]

            
            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)



with st.expander("Obter Detalhes de um Veículo"):
    get_id = st.number_input("ID do Veículo", min_value=1, format="%d")
    if st.button("Buscar Veículo"):
        response = requests.get(f"http://backend:8000/cars/{get_id}")
        if response.status_code == 200:
            cars = response.json()
            df = pd.DataFrame([cars])

            df = df[
                [
                    "car_id",
                    "model",
                    "brand",
                    "model_year",
                    "plate",
                    "kilometers",
                    "status",
                    "created_at",
                ]
            ]

            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)


with st.expander("Deletar Veículo"):
    delete_id = st.number_input("ID do Veículo para Deletar", min_value=1, format="%d")
    if st.button("Deletar Veículo"):
        response = requests.delete(f"http://backend:8000/cars/{delete_id}")
        show_response_message(response)


with st.expander("Atualizar Veículo"):
    with st.form("update_car"):
        update_id = st.number_input("ID do Veículo", min_value=1, format="%d")
        new_model = st.text_input("Novo Nome do Veículo")
        new_brand = st.text_input("Nova Marca do Veículo")
        new_model_year = st.number_input(
            "Novo Ano do Veículo",
        )
        new_plate = st.text_input("Nova Placa do Veículo")
        new_kilometers = st.number_input(
            "Nova Kilometragem do Veículo",
        )
        new_status = st.selectbox(
            "Status",
            ["Novo", "Revisão necessária", "Em uso", "Manutenção necessária", "Parado"],
        )

        update_button = st.form_submit_button("Atualizar Veículo")

        if update_button:
            update_data = {}
            if new_model:
                update_data["Model"] = new_model
            if new_brand:
                update_data["Brand"] = new_brand
            if new_model_year > 1886:
                update_data["Model Year"] = new_model_year
            if new_plate:
                update_data["Plate"] = new_plate
            if new_kilometers > 0:
                update_data["Kilometers"] = new_kilometers
            if new_status:
                update_data["Status"] = new_status

            if update_data:
                response = requests.put(
                    f"http://backend:8000/cars/{update_id}", json=update_data
                )
                show_response_message(response)
            else:
                st.error("Nenhuma informação fornecida para atualização")