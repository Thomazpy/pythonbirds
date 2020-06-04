class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=50):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
        print(Pessoa.metodo_estatico(), tamy.metodo_estatico())
        print(Pessoa.nome_e_atributos_de_classe(), tamy.nome_e_atributos_de_classe())






