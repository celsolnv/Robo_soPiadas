import json
def main():
    with open("piadas.json") as piadas_file:
        piadas = json.load(piadas_file)
        for piada in piadas:
            pontuacoes = [",",".",":",";","!","?"]
            categoria = piada["categoria"] 
            texto = piada['texto']
            # texto = texto.replace("—","-")
            caracter_anterior = ""
            novo_texto = ""
            for caracter in texto:
                if caracter_anterior in pontuacoes:
                    novo_texto += " " + caracter
                else:
                    novo_texto += caracter
                caracter_anterior = caracter
            
            novo_texto = novo_texto.replace("—","-")
            piada["texto"]=novo_texto
            if categoria=="Bebados":
                piada["categoria"]="Bêbados"


        piadas_ref = json.dumps(piadas,ensure_ascii=False).encode('utf8')
        # print(str(piadas_ref.decode()))
        f = open("teste.json","a")
        f.write(str(piadas_ref.decode()))    
main()
                