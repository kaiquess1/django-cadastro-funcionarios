from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class funcionarios(models.Model):
    nome=models.CharField(max_length=50, verbose_name='Nome',null=True)
    sobrenome=models.CharField(max_length=50, verbose_name='Sobrenome',null=True)
    nascimento=models.DateField(verbose_name='Nascimento',null=True)
    endereco=models.CharField(max_length=100,verbose_name='Endereço',null=True)
    email=models.EmailField(max_length=300,verbose_name='Email',null=True)
    phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="O número precisa estar neste formato: \
                    '+99 99 9999-0000'.")

    telefone = models.CharField(verbose_name="Telefone",
                                validators=[phone_regex],
                                max_length=14, null=True, blank=True)
    matricula=models.IntegerField(verbose_name='Matricula',null=True)
    cargo=models.CharField(max_length=60,verbose_name='Cargo',null=True)
    sol='Solteiro'
    cas='casado'
    di='divorciado'
    va=''
    ESTADO_CIVIL=[(va,''),(sol,'Solteiro'),(cas,'Casado'),(di,'Divorciado')]
    estado_civil=models.CharField(max_length=10,choices=ESTADO_CIVIL,default="",verbose_name='Estado Civil')

    class Meta:
        verbose_name_plural='Funcionários'


    def __str__(self):
        return f'{self.nome} {self.sobrenome}'    

    
