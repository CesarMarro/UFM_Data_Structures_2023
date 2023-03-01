from playlist import Node, PlayList, Song


# Songs instantiation
song_a = Song('A',"Tears in Heaven", "Eric Clapton", "Heaven")
song_b = Song('B', "Ophelia", "The Lumineers", "Cleopatra")
song_c = Song('C', "Quesadilla", "Tortolala", "Hits de progra")
song_d = Song('D', "Hamburguesa", "Tortolala", "Hits de progra")
song_e = Song('E', "Stay", "Post Malone", "Tears")
song_f = Song('F', "Chasing cars", "Snow patrol", "Eyes Open")

node_a = Node(song_a)
node_b = Node(song_b)
node_c = Node(song_c)
node_d = Node(song_d)
node_e = Node(song_e)
node_f = Node(song_f)


ll = PlayList()
ll.insert_at_beginning(node_c)
print(ll)
ll.insert_at_beginning(node_b)
print(ll)
ll.insert_at_beginning(node_a)
print(ll)
ll.insert_at_end(node_e)
print(ll)
ll.insert_at_beginning(node_d)
print(ll)

print("---------------------------------------")

ll.play()
ll.show_detail()

ll.previous()
ll.show_detail()

ll.next()
ll.show_detail()
ll.next()
ll.show_detail()
ll.next()
ll.show_detail()
ll.next()
ll.show_detail()
ll.next()

print("---------------------------------------")

print(ll)
ll.Shuffle()
ll.show_detail()

l = ll.PlaylistLen()
print("This playlist has %s songs" % l)

artist = "Tortolala"
ll.SearchByName("Ophelia")
ll.show_detail() 

a = ll.SearchByArtist(artist)

print("Canciones de: %s" % artist)
for i in range (len(a)):
    print(a[i])
