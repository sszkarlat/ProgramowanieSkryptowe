// function logUserData() {
//     var userInput = document.getElementById("userName").value;
//     // console.log(parseInt(userInput));

//     flag = true;
//     for (const char of userInput) {
//         if (!isNaN(parseInt(char))) {
//             console.group("Error-group");
//             console.error("Wprowadziłeś liczbę!");
//             console.groupEnd("Error-group");
//             flag = false
//             break;
//         }
//     }
//     if (flag === true) {
//         console.group("Pass-group");
//         console.log("Wprowadzone dane", userInput)
//         console.groupEnd("Pass-group");
//     }
// }

// Bardzo dobre do przeczytania: https://web.dev/articles/indexeddb?hl=pl
const request = indexedDB.open("dataBase", 1);
let dataBase;

request.onerror = (event) => {
    window.alert("Błąd otwierania bazy danych:", event.target.errorCode);
};

request.onupgradeneeded = (event) => {
    dataBase = event.target.result;

    if (!dataBase.objectStoreNames.contains("Products")) {
        const productsObjectStore = dataBase.createObjectStore("Products", { keyPath: "id", autoIncrement: true });
        productsObjectStore.createIndex("name", "name", { unique: false });
        productsObjectStore.createIndex("quantity", "quantity", { unique: false });
        productsObjectStore.createIndex("price", "price", { unique: false });

        const productsData = [
            { name: "BMW", quantity: 10, price: 800000 },
            { name: "Fiat", quantity: 25, price: 50000 },
            { name: "Mercedes", quantity: 15, price: 1000000 },
            { name: "Volvo", quantity: 8, price: 400000 }
        ];

        productsData.forEach((product) => {
            productsObjectStore.add(product);
        });
    }

    if (!dataBase.objectStoreNames.contains("Customers")) {
        const customersObjectStore = dataBase.createObjectStore("Customers", { keyPath: "id", autoIncrement: true });
        customersObjectStore.createIndex("firstName", "firstName", { unique: false });
        customersObjectStore.createIndex("lastName", "lastName", { unique: false });

        const customersData = [
            { firstName: "Jan", lastName: "Kowalski" },
            { firstName: "Adam", lastName: "Nowak" },
            { firstName: "Monika", lastName: "Miss" }
        ];

        customersData.forEach((customer) => {
            customersObjectStore.add(customer);
        });
    }
};

request.onsuccess = (event) => {
    dataBase = event.target.result;

    const productsTransaction = dataBase.transaction("Products", "readwrite");
    const productsObjectStore = productsTransaction.objectStore("Products");

    const getAllProducts = productsObjectStore.getAll();

    getAllProducts.onsuccess = () => {
        const productsData = getAllProducts.result;
        console.log("Dane produktów:", productsData);
    };
};

request.onerror = (event) => {
    console.error("Błąd otwierania bazy danych:", event.target.errorCode);
};

function executeCommand() {
    var commandLine = document.getElementById("commandLine").value;
    console.log("Komenda:", commandLine);

    var commandParts = commandLine.split(" ");
    var operation = commandParts[0].toLowerCase();

    switch (operation) {
        case "sell":
            sellProduct(commandParts);
            break;
        case "show":
            if (commandParts[1] === "clients") {
                displayCustomers();
            } else if (commandParts[1] === "warehouse") {
                displayInventory();
            } else {
                displayPurchaseHistory(commandParts);
            }
            break;
        default:
            // console.warn("Nieznana operacja:", operation);
            window.alert("Nieznana operacja:", operation);
    }
}

function sellProduct(commandParts) {
    const customerFirstName = commandParts[1];
    const customerLastName = commandParts[2];
    const productName = commandParts[3];
    const quantityToSell = parseInt(commandParts[4]);

    const transaction = dataBase.transaction(["Products", "Customers"], "readwrite");
    const productsObjectStore = transaction.objectStore("Products");
    const customersObjectStore = transaction.objectStore("Customers");

    const getProductRequest = productsObjectStore.index("name").get(productName);
    const getCustomerRequest = customersObjectStore.index("lastName").get(customerLastName);



    getProductRequest.onsuccess = (event) => {
        const product = event.target.result;

        if (quantityToSell > 0) {
            if (product && product.quantity >= quantityToSell) {

                product.quantity -= quantityToSell;
                const updateProductRequest = productsObjectStore.put(product);

                transaction.oncomplete = () => {
                    console.group("Sprzedaż");
                    console.log(`Sprzedano ${quantityToSell} sztuk produktu "${productName}" klientowi "${customerFirstName} ${customerLastName}"`);
                    console.groupEnd();
                };


                updateProductRequest.onerror = (error) => {
                    window.alert("Błąd podczas aktualizacji ilości produktu:", error);
                };

                getCustomerRequest.onsuccess = (event) => {
                    const customer = event.target.result;

                    if (customer) {
                        const purchaseHistory = customer.purchaseHistory || [];
                        purchaseHistory.push({ product: product, quantity: quantityToSell, date: new Date() });
                        customer.purchaseHistory = purchaseHistory;

                        const updateCustomerRequest = customersObjectStore.put(customer);

                        updateCustomerRequest.onerror = (error) => {
                            window.alert("Błąd podczas aktualizacji historii zakupów klienta:", error);
                        };
                    } else {
                        window.alert(`Nie znaleziono klienta o nazwisku ${customerLastName}`);
                    }
                };
            } else {
                window.alert(`Produkt: ${productName} chwilowo niedostępny.`);
            }
        } else if (quantityToSell === 0) {
            window.alert("Nie wolno kupić zerowej liczby sztuk");
        } else {
            window.alert("Nie wolno kupić ujemnej liczby sztuk.");
        }
    };

    getProductRequest.onerror = (error) => {
        window.alert("Błąd podczas pobierania danych produktu:", error);
    };

    getCustomerRequest.onerror = (error) => {
        window.alert("Błąd podczas pobierania danych klienta:", error);
    };
}

function displayCustomers() {
    const transaction = dataBase.transaction("Customers", "readonly");
    const customersObjectStore = transaction.objectStore("Customers");

    const getAllCustomersRequest = customersObjectStore.getAll();

    getAllCustomersRequest.onsuccess = (event) => {
        const customers = event.target.result;

        console.group("Klienci");
        console.log("Lista klientów:");
        customers.forEach((customer) => {
            console.log(`- ${customer.firstName} ${customer.lastName}`);
        });
        console.groupEnd();
    };

    getAllCustomersRequest.onerror = (error) => {
        window.alert("Błąd podczas pobierania listy klientów:", error);
    };
}

function displayPurchaseHistory(commandParts) {
    const customerFirstName = commandParts[1];
    const customerLastName = commandParts[2];

    const transaction = dataBase.transaction(["Products", "Customers"], "readonly");
    // const productsObjectStore = transaction.objectStore("Products");
    const customersObjectStore = transaction.objectStore("Customers");

    const getCustomerRequest = (customersObjectStore.index("firstName").get(customerFirstName), customersObjectStore.index("lastName").get(customerLastName));

    getCustomerRequest.onsuccess = (event) => {
        const customer = event.target.result;

        if (customer) {
            const purchaseHistory = customer.purchaseHistory || [];
            console.group("Historia zakupów");
            console.log(`Historia zakupów klienta: ${customer.firstName} ${customer.lastName}:`);
            let totalCost = 0;

            purchaseHistory.forEach((purchase) => {
                const product = purchase.product;
                const cost = product.price * purchase.quantity;
                totalCost += cost;

                console.log(`- ${product.name}, liczba sztuk: ${purchase.quantity}, cena: ${cost}`);
            });

            console.log(`Sumaryczna cena zakupów: ${totalCost}`);
            console.groupEnd();
        } else {
            window.alert(`Nie znaleziono klienta: ${customerFirstName} ${customerLastName}`);
        }
    };

    getCustomerRequest.onerror = (error) => {
        window.alert("Błąd podczas pobierania danych klienta:", error);
    };
}

function displayInventory() {
    const transaction = dataBase.transaction("Products", "readonly");
    const productsObjectStore = transaction.objectStore("Products");

    const getAllProductsRequest = productsObjectStore.getAll();

    getAllProductsRequest.onsuccess = (event) => {
        const products = event.target.result;

        console.group("Stan magazynu");
        console.log("Ilość dostępnych produktów:");
        products.forEach((product) => {
            console.log(`- ${product.name}: ${product.quantity} sztuk`);
        });
        console.groupEnd();
    };

    getAllProductsRequest.onerror = (error) => {
        window.alert("Błąd podczas pobierania stanu magazynu:", error);
    };
}