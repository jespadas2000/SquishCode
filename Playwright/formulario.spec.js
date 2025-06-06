const { test, expect } = require('@playwright/test');

test.beforeEach(async ({ page }) => {
    await page.goto('https://www.ucm.es/');
});

test.describe('Testing Form', () => {

    test('se llega al la ventana deseada y se buscan las conferencias', async ({ page }) => {
        await page.getByRole('button', { name: 'Agree and close: Agree to our' }).click();
        await page.getByRole('menuitem', { name: 'Universidad' }).click();
        await page.getByRole('menuitem', { name: 'Facultades' }).click();
        await page.getByText('Informática').click();
        
        await page.getByRole('searchbox', { name: 'Buscar en la web' }).fill('conferencias');
        await page.keyboard.press('Enter');

       const data = await page.getByText('6 resultados').isEnabled();
    console.log(data);

    });

    test('buscar conferencias en el browser', async ({ page }) => {

        await page.getByRole('button', { name: 'Agree and close: Agree to our' }).click();
        await page.getByRole('menuitem', { name: 'Universidad' }).click();
        
    });

});