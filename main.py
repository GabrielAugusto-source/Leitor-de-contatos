import os
import requests
from dotenv import load_dotenv
from supabase import create_client

# Carrega variáveis do .env
load_dotenv()

# Inicializa cliente Supabase
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

def main():
    print("Buscando contatos no Supabase...")
    
    try:
        response = supabase.table("contacts").select("*").execute()
        contatos = response.data
    except Exception as e:
        print(f"Erro ao buscar contatos: {e}")
        return
    
    if not contatos:
        print("Nenhum contato encontrado.")
        return
    
    for contato in contatos[:3]:
        nome = contato.get("name")
        telefone = contato.get("phone")
        
        if not nome or not telefone:
            continue
            
        print(f"Tentando enviar para {nome} (Telefone: {telefone})...")
        
        # O .strip() remove qualquer espaço ou quebra de linha acidental do .env
        instance_id = os.getenv("ZAPI_INSTANCE_ID").strip() if os.getenv("ZAPI_INSTANCE_ID") else ""
        token = os.getenv("ZAPI_TOKEN").strip() if os.getenv("ZAPI_TOKEN") else ""

        # DEBUG: Verificação básica
        if not instance_id or not token:
            print("Erro: Instância ou Token não carregados corretamente no .env!")
            return

        # Estrutura padrão da Z-API (Token na URL)
        url = f"https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"
        payload = {"phone": telefone, "message": f"Olá, {nome}, tudo bem com você?"}
        
        try:
            # Enviando a requisição sem o Header 'Client-Token' manual, 
            # pois a Z-API valida pelo token na própria URL
            resposta = requests.post(url, json=payload)
            
            if resposta.status_code == 200:
                print(f"✅ Sucesso: Mensagem enviada para {nome}!")
            else:
                print(f"❌ Falha ao enviar para {nome}. Código: {resposta.status_code}")
                print(f"Resposta da API: {resposta.text}")
                
        except Exception as e:
            print(f"Erro de conexão com o servidor da Z-API: {e}")

    print("Processo finalizado!")

if __name__ == "__main__":
    main()