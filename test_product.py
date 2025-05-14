import pytest
from product import Product
from smartphone import Smartphone
from lawn_grass import LawnGrass
from category import Category

def test_product_creation():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10

def test_smartphone_creation():
    smartphone = Smartphone("Test Phone", "Test Description", 100.0, 10, 95.5, "Model", 256, "Black")
    assert smartphone.name == "Test Phone"
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "Model"
    assert smartphone.memory == 256
    assert smartphone.color == "Black"

def test_lawn_grass_creation():
    grass = LawnGrass("Test Grass", "Test Description", 100.0, 10, "Russia", "7 days", "Green")
    assert grass.name == "Test Grass"
    assert grass.country == "Russia"
    assert grass.germination_period == "7 days"
    assert grass.color == "Green"

def test_product_addition():
    smartphone1 = Smartphone("Phone 1", "Desc", 100.0, 2, 95.5, "Model", 256, "Black")
    smartphone2 = Smartphone("Phone 2", "Desc", 200.0, 3, 95.5, "Model", 256, "Black")
    assert smartphone1 + smartphone2 == 800.0  # 100*2 + 200*3

def test_invalid_product_addition():
    smartphone = Smartphone("Phone", "Desc", 100.0, 2, 95.5, "Model", 256, "Black")
    grass = LawnGrass("Grass", "Desc", 100.0, 2, "Russia", "7 days", "Green")
    with pytest.raises(TypeError):
        smartphone + grass

def test_category_creation():
    category = Category("Test Category", "Test Description")
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category.products) == 0

def test_category_add_product():
    category = Category("Test Category", "Test Description")
    smartphone = Smartphone("Phone", "Desc", 100.0, 2, 95.5, "Model", 256, "Black")
    category.add_product(smartphone)
    assert len(category.products) == 1
    assert category.products[0] == smartphone

def test_category_add_invalid_product():
    category = Category("Test Category", "Test Description")
    with pytest.raises(TypeError):
        category.add_product("Not a product") 