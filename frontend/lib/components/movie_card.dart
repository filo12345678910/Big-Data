import 'package:flutter/material.dart';
import 'package:frontend/models.dart';
import 'package:frontend/pages/seat_selection_page.dart';
import 'package:frontend/services.dart';

class MovieCard extends StatefulWidget {
  final Movie movie;

  const MovieCard({super.key, required this.movie});

  @override
  _MovieCardState createState() => _MovieCardState();
}

class _MovieCardState extends State<MovieCard> {
  Future<List<MovieShow>>? movieShowsList;
  bool isExpanded = false;
  int? hoverIndex;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        setState(() {
          isExpanded = !isExpanded;
          if (isExpanded) {
            movieShowsList ??= fetchMovieShows(movieTitle: widget.movie.title);
          }
        });
      },
      child: Card(
        color: Theme.of(context).colorScheme.secondary,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(16),
          side: BorderSide(
            color: isExpanded
                ? Theme.of(context).colorScheme.tertiary
                : Colors.transparent,
            width: 4,
          ),
        ),
        child: Column(
          children: <Widget>[
            Text(
              widget.movie.title,
              style: Theme.of(context).textTheme.titleMedium,
            ),
            Text(
              'Duration: ${widget.movie.duration}',
              style: Theme.of(context).textTheme.bodyMedium,
            ),
            Text(
              'Genres: ${widget.movie.genres.join(', ')}',
              style: Theme.of(context).textTheme.bodyMedium,
            ),
            Text(
              'Rating: ${widget.movie.rating} / 10',
              style: Theme.of(context).textTheme.bodyMedium,
            ),
            if (isExpanded) ...[
              FutureBuilder<List<MovieShow>>(
                future: movieShowsList,
                builder: (context, snapshot) {
                  if (snapshot.connectionState == ConnectionState.waiting) {
                    return const CircularProgressIndicator();
                  } else if (snapshot.hasError) {
                    return Text(
                      '${snapshot.error}',
                      style: Theme.of(context).textTheme.bodyMedium,
                    );
                  } else {
                    return ListView.builder(
                      shrinkWrap: true,
                      itemCount: snapshot.data!.length,
                      itemBuilder: (context, index) {
                        var show = snapshot.data![index];
                        return MouseRegion(
                          cursor: SystemMouseCursors.click,
                          onHover: (_) {
                            setState(() {
                              hoverIndex = index;
                            });
                          },
                          onExit: (_) {
                            setState(() {
                              hoverIndex = null;
                            });
                          },
                          child: GestureDetector(
                            onTap: () {
                              Navigator.push(
                                context,
                                MaterialPageRoute(
                                  builder: (context) =>
                                      SeatSelectionPage(movieShow: show),
                                ),
                              );
                            },
                            child: Container(
                              padding: const EdgeInsets.all(8.0),
                              decoration: BoxDecoration(
                                border: Border.all(
                                  color: hoverIndex == index
                                      ? Theme.of(context).colorScheme.tertiary
                                      : Colors.transparent,
                                  width: 4,
                                ),
                              ),
                              child: Text(
                                '${show.showTime.day}.${show.showTime.month}.${show.showTime.year} - ${show.showTime.hour}:${show.showTime.minute}',
                                style: Theme.of(context).textTheme.bodyMedium,
                              ),
                            ),
                          ),
                        );
                      },
                    );
                  }
                },
              ),
            ],
          ],
        ),
      ),
    );
  }
}
