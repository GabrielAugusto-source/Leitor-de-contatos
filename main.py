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
    
    
    for contato in contatos[:3]:
        nome = contato.get("name")
        telefone = contato.get("phone")
        
        if not nome or not telefone:
            continue
            
        print(f"Enviando para {nome}...")
        
        
        url = f"https://api.z-api.io/instances/{os.getenv('ZAPI_INSTANCE_ID')}/token/{os.getenv('ZAPI_TOKEN')}/send-text"
        payload = {"phone": telefone, "message": f"Olá, {nome}, tudo bem com você?"}
        
        try:
            requests.post(url, json=payload)
        except Exception as e:
            print(f"Erro ao enviar para {nome}: {e}")

    print("Processo finalizado!")

if __name__ == "__main__":
    main()