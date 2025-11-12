from typing import Optional

from src.core.entities.product import Product
from src.core.exceptions import ProductNotFound
from src.core.interfaces.product_repository import ProductRepository
from src.core.interfaces.usecase_interface import UseCase

class UpdateProductUseCase(UseCase):
    """Use case responsible for listing all products."""

    def __init__(self, repository: ProductRepository):
        self._repository = repository

    def execute(
        self, nome, quantidade: Optional[int], valor: Optional[float]
    ) -> Product:
        foundProduct = self._repository.get_by_name(nome)
        if not foundProduct:
            raise ProductNotFound(f"Produto '{nome}' não encontrado.")

        if quantidade is None:
            quantidade = foundProduct.quantidade
        if valor is None:
            valor = foundProduct.valor

        product = Product(nome=nome, quantidade=quantidade, valor=valor)
        return self._repository.update(product)