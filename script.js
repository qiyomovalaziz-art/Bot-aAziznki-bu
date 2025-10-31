let tg = window.Telegram.WebApp;
tg.expand();

let balance = 0;
let balanceElement = document.getElementById("balance");

function updateBalance(amount) {
  balance += amount;
  balanceElement.innerText = balance;
}

function sendMoney() {
  alert("💸 Pul yuborish funksiyasi tez orada qo'shiladi!");
}

function exchange() {
  alert("🔁 Almashtirish funksiyasi hozircha test holatda!");
}

function mining() {
  updateBalance(1);
  alert("✨ Siz 1 ta token oldingiz!");
}

function buyUC() {
  alert("🎮 UC sotib olish tez orada yo‘lga qo‘yiladi!");
}

function openTasks() {
  alert("📋 Bugungi topshiriqlar: \n1. Botni ulashish\n2. Do‘stni taklif qilish");
}
