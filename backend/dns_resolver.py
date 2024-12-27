# import socket
# import logging
# from cache import Cache
# from dns_advanced_addons import AdvancedDNSAddons


# def resolve_recursive(domain, query_type):
#     """Resolve the domain name recursively."""
#     try:
#         dns_server = "8.8.8.8"  # Google's public DNS server
#         query = build_dns_query(domain, query_type)
#         with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#             s.settimeout(5)  # 5-second timeout
#             s.sendto(query, (dns_server, 53))
#             response, _ = s.recvfrom(512)
#         return parse_dns_response(response)
#     except socket.timeout:
#         logging.error(f"Timeout while resolving {domain}")
#         return None
#     except Exception as e:
#         logging.error(f"Error during recursive resolution of {domain}: {e}")
#         return None


# def resolve_iterative(domain, query_type):
#     """Resolve the domain name iteratively."""
#     try:
#         root_servers = ["198.41.0.4", "199.9.14.201"]  # Example root servers
#         for server in root_servers:
#             query = build_dns_query(domain, query_type)
#             with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#                 s.settimeout(5)
#                 s.sendto(query, (server, 53))
#                 response, _ = s.recvfrom(512)
#                 result = parse_dns_response(response)
#                 if result:
#                     return result
#         logging.error(f"Failed to resolve {domain} iteratively.")
#         return None
#     except socket.timeout:
#         logging.error(f"Timeout while resolving {domain}")
#         return None
#     except Exception as e:
#         logging.error(f"Error during iterative resolution of {domain}: {e}")
#         return None


# def build_dns_query(domain, query_type):
#     """Construct a DNS query for the given domain and type."""
#     query_types = {"A": 1, "AAAA": 28, "MX": 15, "CNAME": 5}
#     qtype = query_types.get(query_type.upper(), 1)

#     header = b"\xaa\xaa"  # ID (arbitrary)
#     header += b"\x01\x00"  # Flags (standard query)
#     header += b"\x00\x01"  # QDCOUNT (1 question)
#     header += b"\x00\x00"  # ANCOUNT
#     header += b"\x00\x00"  # NSCOUNT
#     header += b"\x00\x00"  # ARCOUNT

#     question = b""
#     for part in domain.split("."):
#         question += bytes([len(part)]) + part.encode()
#     question += b"\x00"  # End of QNAME
#     question += qtype.to_bytes(2, byteorder="big")  # QTYPE
#     question += b"\x00\x01"  # QCLASS (IN)

#     return header + question


# def parse_dns_response(response):
#     """Parse the DNS response and extract the relevant information."""
#     header = response[:12]
#     question = response[12:]
#     answers = []

#     qdcount = int.from_bytes(header[4:6], byteorder="big")
#     ancount = int.from_bytes(header[6:8], byteorder="big")

#     offset = 0
#     for _ in range(qdcount):
#         while question[offset] != 0:
#             offset += question[offset] + 1
#         offset += 5  # Skip null byte and QTYPE/QCLASS

#     for _ in range(ancount):
#         offset += 2  # Name pointer
#         rtype = int.from_bytes(question[offset : offset + 2], byteorder="big")
#         offset += 8  # Skip RCLASS, TTL
#         rdlength = int.from_bytes(question[offset : offset + 2], byteorder="big")
#         offset += 2
#         rdata = question[offset : offset + rdlength]
#         offset += rdlength

#         if rtype == 1:  # A record
#             ip = ".".join(map(str, rdata))
#             answers.append(ip)
#         elif rtype == 5:  # CNAME record
#             cname = ""
#             i = 0
#             while rdata[i] != 0:
#                 length = rdata[i]
#                 i += 1
#                 cname += rdata[i : i + length].decode() + "."
#                 i += length
#             answers.append(cname[:-1])

#     return answers


# def resolve(domain, query_type="A", method="recursive"):
#     """Resolve a domain name using the specified method."""
#     cache = Cache()
#     cached_result = cache.get(domain, query_type)
#     if cached_result:
#         logging.info(f"Cache hit for {domain} ({query_type})")
#         return cached_result

#     logging.info(f"Resolving {domain} ({query_type}) using {method} method.")
#     if method == "recursive":
#         result = resolve_recursive(domain, query_type)
#     elif method == "iterative":
#         result = resolve_iterative(domain, query_type)
#     else:
#         logging.error("Unknown resolution method.")
#         return None

#     if result:
#         cache.add(domain, query_type, result)
#     return result


# addons = AdvancedDNSAddons()

# # Check rate-limiting
# client_ip = "192.168.1.1"
# if addons.is_rate_limited(client_ip):
#     print("Rate limit exceeded for", client_ip)
# else:
#     result = addons.dns_over_https("example.com", "A")
#     print("DoH Result:", result)
#     addons.log_query("example.com", "A", client_ip)
#     addons.visualize_logs()


# ======================================================================

import socket
import dns.resolver


def resolve(domain, query_type, method):
    # If the query type is PTR, handle reverse DNS lookup
    if query_type == "PTR":
        return resolve_reverse_dns(domain)

    # Otherwise, resolve using standard DNS methods
    if method == "recursive":
        return resolve_recursive(domain, query_type)
    elif method == "iterative":
        return resolve_iterative(domain, query_type)


def resolve_recursive(domain, query_type):
    try:
        resolver = dns.resolver.Resolver()
        answers = resolver.resolve(domain, query_type)
        return [answer.to_text() for answer in answers]
    except dns.resolver.NoAnswer:
        return []
    except dns.resolver.NXDOMAIN:
        return ["Domain does not exist."]
    except Exception as e:
        return [f"Error: {str(e)}"]


def resolve_iterative(domain, query_type):
    try:
        resolver = dns.resolver.Resolver()
        answers = resolver.resolve(domain, query_type)
        return [answer.to_text() for answer in answers]
    except dns.resolver.NoAnswer:
        return []
    except dns.resolver.NXDOMAIN:
        return ["Domain does not exist."]
    except Exception as e:
        return [f"Error: {str(e)}"]


def resolve_reverse_dns(ip_address):
    try:
        host = socket.gethostbyaddr(ip_address)[0]
        return [host]
    except socket.herror:
        return ["No PTR record found"]
