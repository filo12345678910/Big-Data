import 'package:flutter/material.dart';
import 'pages/movies_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
          brightness: Brightness.light,
          colorScheme: const ColorScheme.light(
            onSurface: Color(0x05070701),
            surface: Color(0xffaac1a7),
            primary: Color(0xff74a463),
            secondary: Color(0xffa7ccb6),
            tertiary: Color(0xff58B69A),
          ),
          useMaterial3: true,
          textTheme: const TextTheme(
              titleLarge: TextStyle(
                  fontSize: 32,
                  color: Color.fromRGBO(5, 7, 7, 1),
                  fontWeight: FontWeight.bold),
              titleMedium: TextStyle(
                  fontSize: 24,
                  color: Color.fromRGBO(5, 7, 7, 1),
                  fontWeight: FontWeight.bold),
              titleSmall: TextStyle(
                  fontSize: 20,
                  color: Color.fromRGBO(5, 7, 7, 1),
                  fontWeight: FontWeight.bold),
              bodyLarge:
                  TextStyle(fontSize: 16, color: Color.fromRGBO(5, 7, 7, 1)),
              bodyMedium:
                  TextStyle(fontSize: 14, color: Color.fromRGBO(5, 7, 7, 1)),
              bodySmall:
                  TextStyle(fontSize: 12, color: Color.fromRGBO(5, 7, 7, 1)))),
      home: const Scaffold(
        body: MoviesPage(title: 'Movies'),
      ),
    );
  }
}
