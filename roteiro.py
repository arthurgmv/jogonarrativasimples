
def jogo():
    resposta = input ("Você gostaria de jogar? (s/n)")
    if resposta.lower() == "s":
        print ("Bem-vindo ao jogo")
        start=True
        inventory=[]
    else: print ("Está bem, quem sabe na próxima")
    
   
    if start==True:
        print('''Olá estranho, você acaba de entrar em um mundo totalmente novo.''')
        print ('''Talvez você não saiba como veio parar aqui, mas nós estávamos lhe observando.''')
        print ('''Bem-vindo à Alpha, o mundo digital, chamamos você aqui, pois mesmo sendo do mundo físico...''')
        print ("Você é nossa única esperança!")
        print ('''ESSA NÃO! MÁS COMO? 
        
        CORRA! Ahhhrg...''')
        choice0 = input ('''- O velho narrador foi atacado por um demônio, ele está olhando diretamente para você, 
        você pode enfrentar o demônio ou fugir. Aperte L para enfrentar o monstro e F para fugir. (l/f)      
        ''')
        
    if choice0.lower()== "f":
            choice0=True
            print ('''Você correu com todas as suas forças,o demônio com seus olhos vermelhos olhava fitammente para você, mas parabéns, você fugiu!
            Ao ver uma porta a sua frente você passa por ela e encontra um machado''')
            inventory.append ("Machado")
            choice1 = input ("Você agora tem um machado que pode ser usado para enfrentar o demônio, você quer enfrentá-lo? (s/n)")
            if choice1== "s":
                print ('''Você respira fundo, segura o machado bem firme e abre de novo a porta. Ele está lá, olhando para você com seus olhos vermelhos e seu sorriso maligno
                você cria coragem e avança, mete uma machadada na cabeça dele com tamanha energia que seu machado fica preso no crânio dele.- Você imediatamente começa a ouvir 
                uma voz vinda do além, como que de algum lugar acima de você...
                - Parabéns jovem guerreiro, este foi o seu primeiro teste! Ainda há muitos seres malignos para derrotar
                e livrar Alpha da desolação eterna''')
                print ("Parabéns, você finalizou a demo do jogo")
                fimA = input ("Aperte 'f' para sair (f)")
            else:
                print ('''Você demorou muito ficou tremento sem saber o que fazer...
                A porta se abre e ele lhe ataca por trás, você não teve chance alguma de se defender...''')
                print ('''
                
                
                GAME OVER ''')
                fimB = input ("Aperte 'f' para sair (f)")        
    else: 
        print ('''Você não foi forte o bastante, 
        
        GAME OVER''')
        fim = input ("Aperte 'f' para sair (f)")
       
jogo()