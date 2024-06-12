import 'package:flutter/material.dart';
import 'package:frontend/models.dart';
import 'package:frontend/services.dart';
import 'package:frontend/components/movie_card.dart';

class MoviesPage extends StatefulWidget {
  const MoviesPage({super.key, required this.title});
  final String title;

  @override
  State<MoviesPage> createState() => _MoviesPageState();
}

class _MoviesPageState extends State<MoviesPage> {
  Future<List<Movie>> moviesList = fetchMovies();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.secondary,
        title: Text(
          widget.title,
          style: Theme.of(context).textTheme.titleLarge,
        ),
        centerTitle: true,
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.only(top: 64.0, left: 128.0, right: 128.0),
          child: FutureBuilder<List<Movie>>(
            future: moviesList,
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.waiting) {
                return const CircularProgressIndicator();
              } else if (snapshot.hasError) {
                return Text('Error: ${snapshot.error}');
              } else {
                return GridView.count(
                  crossAxisSpacing: 32,
                  mainAxisSpacing: 32,
                  crossAxisCount: 4,
                  childAspectRatio: 0.8,
                  children: snapshot.data!.map((movie) {
                    return MovieCard(
                      movie: movie,
                    );
                  }).toList(),
                );
              }
            },
          ),
        ),
      ),
    );
  }
}
