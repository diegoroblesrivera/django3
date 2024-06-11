
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20, null=True)),
                ('apellido_materno', models.CharField(max_length=20, null=True)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=45, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ramo',
            fields=[
                ('id_ramo', models.AutoField(db_column='idRamo', primary_key=True, serialize=False)),
                ('ramo', models.CharField(max_length=20)),
                ('creditos', models.IntegerField()),
                ('escuela', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id_seccion', models.AutoField(db_column='idSeccion', primary_key=True, serialize=False)),
                ('codigo_seccion', models.CharField(max_length=20)),
                ('id_ramo', models.ForeignKey(db_column='idRamo', on_delete=django.db.models.deletion.CASCADE, to='alumnos.ramo')),
            ],
        ),
        migrations.CreateModel(
            name='AlumnoSeccion',
            fields=[
                ('id_alumnoseccion', models.AutoField(db_column='idAlumnoSeccion', primary_key=True, serialize=False)),
                ('id_alumno', models.ForeignKey(db_column='idRamo', on_delete=django.db.models.deletion.CASCADE, to='alumnos.alumno')),
                ('id_seccion', models.ForeignKey(db_column='rut', on_delete=django.db.models.deletion.CASCADE, to='alumnos.seccion')),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='id_genero',
            field=models.ForeignKey(db_column='idGenero', null=True, on_delete=django.db.models.deletion.CASCADE, to='alumnos.genero'),
        ),
    ]
