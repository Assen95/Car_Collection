from django.core import validators
from django.db import models


class Profile(models.Model):
    MAX_LEN_USER = 10
    MIN_LEN_USER = 2
    MAX_LEN_PASSWORD = 30
    MAX_LEN_F_NAME = 30
    MAX_LEN_L_NAME = 30
    MIN_LEN_AGE = 18

    username = models.CharField(
        max_length=MAX_LEN_USER,
        validators=(
            validators.MinLengthValidator(2, message='The username must be a minimum of 2 chars'),
        ),
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        validators=(
            validators.MinValueValidator(MIN_LEN_AGE),
        ),
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=MAX_LEN_PASSWORD, # TODO: Remember to add widget for PasswordInput!
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=MAX_LEN_F_NAME,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=MAX_LEN_L_NAME,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    MAX_TYPE_CAR_LEN = 10
    MAX_MODEL_CAR_LEN = 20
    MIN_MODEL_CAR_LEN = 2
    MIN_PRICE_CAR_LEN = 1

    SPORTS = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    VEHICLES = (
        (SPORTS, SPORTS),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    type = models.CharField(
        max_length=MAX_TYPE_CAR_LEN,
        choices=VEHICLES,
        null=False,
        blank=False
    )
    model_car = models.CharField(
        max_length=MAX_MODEL_CAR_LEN,
        validators=(
            validators.MinLengthValidator(MIN_MODEL_CAR_LEN),
        ),
        null=False,
        blank=False,
    )
    year = models.IntegerField(
        validators=(

        ),
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        validators=(
            validators.MinValueValidator(MIN_PRICE_CAR_LEN),
        ),
        null=False,
        blank=False,
    )

    d