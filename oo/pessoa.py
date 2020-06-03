class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=50):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    thomaz = Pessoa(nome='Thomaz')
    tamy = Pessoa(thomaz, nome='Tamy')
    print(Pessoa.cumprimentar(tamy))
    print(id(tamy))
    print(tamy.cumprimentar())
    print(tamy.nome)
    print(tamy.idade)
    for filho in tamy.filhos:
        print(filho.nome)
        tamy.sobrenome = 'Cardoso'
        del tamy.filhos
        tamy.olhos = 1
        del tamy.olhos
        print(tamy.__dict__)
        print(thomaz.__dict__)
        Pessoa.olhos = 3
        print(Pessoa.olhos)
        print(tamy.olhos)
        print(thomaz.olhos)
        print(id(Pessoa.olhos), id(tamy.olhos), id(thomaz.olhos))






