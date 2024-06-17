import qrcode #gerador de qrcode para o projeto de açaiteria @guto_marmiroli

guto = input('Digite a url desejada: ')

meu_qrcode = qrcode.make(guto)
meu_qrcode.save("qrcode.png")
print('Qrcode gerado com sucesso! qrcode.png')