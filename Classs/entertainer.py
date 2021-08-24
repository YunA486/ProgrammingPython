class Entertainer:  #키, 얼굴, 인성
    def __init__(self, name):
        self.name = name
        pass

    def set_height(self, height):
        self.height = height

    def set_face(self, face):
        self.face = face

    def set_kind(self, kind):   #인성
        self.kind = kind

    def set_name(self, name):
        self.name = name

    # def info(self):
    #     print(f'이름 : {self.name}\t키 : {self.height}\t얼굴 : {self.face}\t인성 : {self.kind}')

    def __str__(self):
        return f'이름 : {self.name}\t키 : {self.height}\t얼굴 : {self.face}\t인성 : {self.kind}'


아이유 = Entertainer('아이유')
# 아이유.set_name('이지은')
아이유.set_height('161cm')
아이유.set_face('형섭쌤 이상형')
아이유.set_kind('that\'s very good')
print(아이유)

뷔 = Entertainer('뷔')
뷔.set_height('179cm')
뷔.set_face('handsome~~')
뷔.set_kind('That\'s very good and cute')
print(뷔)

class Singer(Entertainer):
    def __init__(self, name, song):
        super().__init__(name)      # self.name = name
        self.song = song

    def __str__(self):
        return super().__str__() + f'\t대표곡 : {self.song}'

class Talent(Entertainer):
    def __init__(self, name, drama):
        super().__init__(name)
        self.drama = drama

    def __str__(self):
        return super().__str__() + f'\t드라마 : {self.drama}'

뷔 = Singer('뷔', 'Love Maze')
뷔.set_height('179cm')
뷔.set_face('handsome~~')
뷔.set_kind('That\'s very good and cute')
print(뷔)

RM = Singer('RM', 'Answer: love myself')
RM.set_height('179cm')
RM.set_face('soso~~')
RM.set_kind('That\'s very good and cute')
print(RM)

현빈 = Talent('현빈', '사랑의 불시착')
현빈.set_height('185cm')
현빈.set_face('handsome~~')
현빈.set_kind('good~~')
print(현빈)

방탄소년단 = []
방탄소년단.append(뷔)
방탄소년단.append(RM)

print(방탄소년단)