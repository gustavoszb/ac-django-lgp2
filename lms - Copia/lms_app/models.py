from django.db import models

# Create your models here.

class Professor(models.Model):
    def __str__(self):
                

        return self.nome + self.email
    
    def save(self):
        if self.email == None or self.email == '' :
            self.email = 'email nao fornecido'
        print('estou salvando!')
        super(Professor,self).save()


    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)
    
