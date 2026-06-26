import os
import requests
from dotenv import load_dotenv
from supabase import create_client


load_dotenv()


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
        
        
        url = f"https://api.z-api.io/instances/{os.getenv('ZAPI_INSTANCE_ID')}/token/{os.getenv('ZAPI_TOKEN')}/send-text"
        payload = {"phone": telefone, "message": f"Olá, {nome}, tudo bem com você?"}
        
        try:
            
            resposta = requests.post(url, json=payload)
            
            
            if resposta.status_code == 200:
                print(f"✅ Sucesso: Mensagem enviada para {nome}!")
            else:
                
                print(f"❌ Falha ao enviar para {nome}. Código: {resposta.status_code}")
                print(f"Detalhe do erro: {resposta.text}")
                
        except Exception as e:
            print(f"Erro de conexão com o servidor da Z-API: {e}")

    print("Processo finalizado!")

if __name__ == "__main__":
    main()