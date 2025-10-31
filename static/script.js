const API_URL = "https://web-production-cbda.up.railway.app";
const tg = window.Telegram.WebApp;
const user_id = tg.initDataUnsafe?.user?.id || "demo_user";

const balanceText = document.getElementById("balance");
const coinImage = document.getElementById("coinImage");

// 🔹 Bosilganda tanga qo‘shish
coinImage.addEventListener("click", async () => {
  try {
    const res = await fetch(`${API_URL}/add_coin`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id }),
    });
    const data = await res.json();
    balanceText.textContent = data.balance;
  } catch (err) {
    console.error("Xatolik:", err);
  }
});

// 🔹 Balansni yuklash (ilova ochilganda)
async function loadBalance() {
  try {
    const res = await fetch(`${API_URL}/get_balance?user_id=${user_id}`);
    const data = await res.json();
    balanceText.textContent = data.balance;
  } catch (err) {
    console.error("Balans olishda xatolik:", err);
  }
}

loadBalance();
