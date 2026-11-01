import heapq
from collections import defaultdict

# ------------------ Node Class ------------------
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For priority queue comparison (heapq)
    def __lt__(self, other):
        return self.freq < other.freq


# ------------------ Build Huffman Tree ------------------
def build_huffman_tree(text):
    # Count frequency of each character
    freq = defaultdict(int)
    for ch in text:
        freq[ch] += 1

    # Create a heap (priority queue)
    heap = [Node(ch, f) for ch, f in freq.items()]
    heapq.heapify(heap)

    # Merge nodes until one tree remains
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # Return the root node
    return heap[0]


# ------------------ Generate Huffman Codes ------------------
def generate_codes(root, current_code="", codes={}):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code
        return

    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)
    return codes


# ------------------ Encode Text ------------------
def encode_text(text, codes):
    return ''.join(codes[ch] for ch in text)


# ------------------ Decode Text ------------------
def decode_text(encoded_text, root):
    decoded = ""
    node = root
    for bit in encoded_text:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            decoded += node.char
            node = root
    return decoded


# ------------------ Visualize Huffman Tree ------------------
def visualize_tree(node, indent="", last=True):
    if node is not None:
        print(indent, "└─ " if last else "├─ ", end="")
        if node.char is not None:
            print(f"'{node.char}' ({node.freq})")
        else:
            print(f"({node.freq})")
        indent += "   " if last else "│  "
        visualize_tree(node.left, indent, False)
        visualize_tree(node.right, indent, True)


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    text = "aaabbcddddeee"
    print("Original text:", text)

    # Build Huffman Tree
    root = build_huffman_tree(text)

    # Generate Codes
    codes = generate_codes(root)
    print("\nGenerated Huffman Codes:")
    for ch, code in codes.items():
        print(f"{ch}: {code}")

    # Encode
    encoded = encode_text(text, codes)
    print("\nEncoded text:", encoded)

    # Decode
    decoded = decode_text(encoded, root)
    print("\nDecoded text:", decoded)

    # Visualize Huffman Tree
    print("\nHuffman Tree Structure:")
    visualize_tree(root)
