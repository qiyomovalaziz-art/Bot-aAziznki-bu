import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main() {
  runApp(AzizbekCurptoApp());
}

class AzizbekCurptoApp extends StatefulWidget {
  @override
  _AzizbekCurptoAppState createState() => _AzizbekCurptoAppState();
}

class _AzizbekCurptoAppState extends State<AzizbekCurptoApp> {
  int _balance = 0;
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadBalance();
  }

  // 🔹 Balansni saqlash va o‘qish (mahalliy xotira orqali)
  Future<void> _loadBalance() async {
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _balance = prefs.getInt('balance') ?? 0;
      _isLoading = false;
    });
  }

  Future<void> _incrementBalance() async {
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _balance++;
    });
    await prefs.setInt('balance', _balance);
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) {
      return const MaterialApp(
        home: Scaffold(
          backgroundColor: Colors.black,
          body: Center(
            child: CircularProgressIndicator(color: Colors.cyanAccent),
          ),
        ),
      );
    }

    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.black,
        body: SafeArea(
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const SizedBox(height: 20),

                // 🔹 Rasm — bosilganda hech qanday animatsiya yoki kichrayish yo‘q
                GestureDetector(
                  onTap: _incrementBalance,
                  child: Container(
                    width: 220,
                    height: 220,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      border: Border.all(
                        color: Colors.cyanAccent,
                        width: 3,
                      ),
                      image: const DecorationImage(
                        image: AssetImage('assets/logo.png'),
                        fit: BoxFit.cover,
                      ),
                    ),
                  ),
                ),

                const SizedBox(height: 15),
                const Text(
                  'AZIZBEK CURUPTO',
                  style: TextStyle(
                    fontSize: 22,
                    color: Colors.cyanAccent,
                    fontWeight: FontWeight.bold,
                  ),
                ),

                const SizedBox(height: 20),

                // 🔹 Balans ko‘rsatish joyi
                Container(
                  margin: const EdgeInsets.symmetric(horizontal: 25),
                  padding: const EdgeInsets.all(20),
                  decoration: BoxDecoration(
                    color: Colors.grey[900],
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: Column(
                    children: [
                      const Text(
                        'Umumiy balans',
                        style: TextStyle(color: Colors.white, fontSize: 18),
                      ),
                      const SizedBox(height: 10),
                      Text(
                        '$_balance',
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 36,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),

                const SizedBox(height: 30),

                // 🔹 Tugmalar
                Wrap(
                  alignment: WrapAlignment.center,
                  spacing: 15,
                  runSpacing: 15,
                  children: [
                    _buildButton(Icons.send, 'Yuborish'),
                    _buildButton(Icons.swap_horiz, 'Almashtirish'),
                    _buildButton(Icons.auto_awesome, 'Mayning'),
                    _buildButton(Icons.shopping_cart, 'UC sotib olish'),
                    _buildButton(Icons.list_alt, 'Topshiriqlar +1'),
                  ],
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildButton(IconData icon, String text) {
    return Container(
      width: 150,
      height: 50,
      decoration: BoxDecoration(
        color: Colors.grey[850],
        borderRadius: BorderRadius.circular(10),
      ),
      child: Center(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, color: Colors.white),
            const SizedBox(width: 6),
            Text(
              text,
              style: const TextStyle(color: Colors.white),
            ),
          ],
        ),
      ),
    );
  }
}
