document.addEventListener("DOMContentLoaded", () => {
  const logo = document.getElementById("logo");
  const balanceDisplay = document.getElementById("balance");

  logo.addEventListener("click", async () => {
    const res = await fetch("/add_coin", { method: "POST" });
    const data = await res.json();
    balanceDisplay.textContent = data.balance;
  });
});
