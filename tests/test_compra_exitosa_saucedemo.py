# Importamos Page para que Playwright entienda que vamos a controlar una página del navegador.
# También importamos expect para hacer validaciones, es decir, comprobar que algo ocurrió correctamente.
from playwright.sync_api import Page, expect


# Esta función es nuestro caso de prueba automatizado.
# Pytest detecta esta prueba porque el nombre comienza con test_.
def test_compra_exitosa_saucedemo(page: Page):

    # Abrimos la página web de prueba Sauce Demo.
    page.goto("https://www.saucedemo.com/")

    # Validamos que la página cargó correctamente revisando el título del navegador.
    expect(page).to_have_title("Swag Labs")

    # Escribimos el usuario válido en el campo username.
    page.locator("[data-test='username']").fill("standard_user")

    # Escribimos la contraseña válida en el campo password.
    page.locator("[data-test='password']").fill("secret_sauce")

    # Hacemos clic en el botón Login para entrar a la aplicación.
    page.locator("[data-test='login-button']").click()

    # Validamos que entramos correctamente revisando que aparezca el texto Products.
    expect(page.locator(".title")).to_have_text("Products")

    # Agregamos al carrito el producto Sauce Labs Backpack.
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    # Validamos que el carrito muestre el número 1, indicando que hay un producto agregado.
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    # Hacemos clic en el ícono del carrito para revisar la compra.
    page.locator(".shopping_cart_link").click()

    # Validamos que estamos en la pantalla del carrito.
    expect(page.locator(".title")).to_have_text("Your Cart")

    # Hacemos clic en Checkout para iniciar el proceso de compra.
    page.locator("[data-test='checkout']").click()

    # Escribimos un nombre ficticio para completar el formulario de compra.
    page.locator("[data-test='firstName']").fill("Ricardo")

    # Escribimos un apellido ficticio para completar el formulario de compra.
    page.locator("[data-test='lastName']").fill("Tapia")

    # Escribimos un código postal ficticio.
    page.locator("[data-test='postalCode']").fill("8320000")

    # Hacemos clic en Continue para pasar al resumen final de la compra.
    page.locator("[data-test='continue']").click()

    # Validamos que estamos en la pantalla de resumen de la compra.
    expect(page.locator(".title")).to_have_text("Checkout: Overview")

    # Finalizamos la compra haciendo clic en Finish.
    page.locator("[data-test='finish']").click()

    # Validamos que aparece el mensaje final de compra exitosa.
    expect(page.locator("[data-test='complete-header']")).to_have_text("Thank you for your order!")

    # Guardamos una captura de pantalla como evidencia del resultado final.
    page.screenshot(path="evidence/screenshots/compra_exitosa.png", full_page=True)